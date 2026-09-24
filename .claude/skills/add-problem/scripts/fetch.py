"""Get a LeetCode problem from the LeetCode GraphQL API and print it as JSON.

Usage: uv run python .claude/skills/add-problem/scripts/fetch.py <url-or-slug>

The JSON has these keys:
  id, title, slug, difficulty, category, paid, url, folder,
  content (the HTML problem statement),
  schema (table -> column -> SQL type),
  examples (list of {"headers": ..., "rows": ...}, one item for each example input).
"""

import json
import re
import sys
import urllib.request

API = "https://leetcode.com/graphql"
QUERY = """
query q($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionFrontendId title titleSlug difficulty categoryTitle isPaidOnly
    content exampleTestcases metaData
  }
}
"""


def slug_from(arg: str) -> str:
    match = re.search(r"leetcode\.(?:com|cn)/problems/([^/?#]+)", arg)
    return match.group(1) if match else arg.strip("/")


def fetch(slug: str) -> dict:
    body = json.dumps({"query": QUERY, "variables": {"titleSlug": slug}}).encode()
    request = urllib.request.Request(
        API,
        data=body,
        headers={
            "Content-Type": "application/json",
            "Referer": f"https://leetcode.com/problems/{slug}/",
            "User-Agent": "Mozilla/5.0",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        question = json.load(response)["data"]["question"]
    if question is None:
        sys.exit(f"No problem found for slug {slug!r}.")
    return question


def parse_examples(text: str | None) -> list[dict]:
    """Each example input is one JSON object. LeetCode puts one object on each line."""
    examples = []
    for line in (text or "").splitlines():
        line = line.strip()
        if line:
            examples.append(json.loads(line))
    return examples


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    q = fetch(slug_from(sys.argv[1]))
    meta = json.loads(q["metaData"] or "{}")
    number = int(q["questionFrontendId"])
    result = {
        "id": number,
        "title": q["title"],
        "slug": q["titleSlug"],
        "difficulty": q["difficulty"],
        "category": q["categoryTitle"],
        "paid": q["isPaidOnly"],
        "url": f"https://leetcode.com/problems/{q['titleSlug']}/",
        "folder": f"p{number:04d}_{q['titleSlug'].replace('-', '_')}",
        "schema": meta.get("database_schema", {}),
        "examples": parse_examples(q["exampleTestcases"]),
        "content": q["content"],
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
