# Golden Dataset: Expected Results (calculated by hand)

## Quoted totals (sum of line totals)

| Vendor | Quoted total |
|---|---:|
| A | 1,201,000 |
| B | 1,059,000 |
| C | 1,200,000 |

## Leveled Price

| Vendor | Scaffolding | Adjustment | Leveled low | Leveled base | Leveled high | Partial? |
|---|---|---|---:|---:|---:|---|
| A | Included | none | 1,201,000 | 1,201,000 | 1,201,000 | No |
| B | Explicitly excluded | 80,000 / 82,500 / 85,000 (estimated from other vendors) | 1,139,000 | 1,141,500 | 1,144,000 | Yes |
| C | Included | none | 1,200,000 | 1,200,000 | 1,200,000 | No |

How the numbers come out:
- A = 76,000 + 650,000 + 120,000 + 80,000 + 275,000 = 1,201,000
- B = 74,000 + 620,000 + 115,000 + 250,000 = 1,059,000
- C = 77,000 + 640,000 + 118,000 + 85,000 + 280,000 = 1,200,000
- B's scaffolding estimate comes from A (80,000) and C (85,000): low 80,000, base (average) 82,500, high 85,000.
- B leveled: 1,059,000 + 80,000 = 1,139,000 / + 82,500 = 1,141,500 / + 85,000 = 1,144,000

## Specification check

| Vendor | Item | Required | Offered | Result |
|---|---|---|---|---|
| A | Cement | OPC 53 grade | OPC 53 grade | COMPLIANT |
| A | TMT Steel | Fe500D | Fe500D | COMPLIANT |
| A | Ready Mix Concrete | M25 | M25 | COMPLIANT |
| B | Cement | OPC 53 grade | OPC 53 grade | COMPLIANT |
| B | TMT Steel | Fe500D | (not stated) | MISSING_INFORMATION |
| B | Ready Mix Concrete | M25 | M20 | DOWNGRADE (mandatory fail) |
| C | Cement | OPC 53 grade | OPC 53 grade | COMPLIANT |
| C | TMT Steel | Fe500D | Fe500D | COMPLIANT |
| C | Ready Mix Concrete | M25 | M25 | COMPLIANT |

## Eligibility and recommendation

| Vendor | Eligibility | Recommendation | Role |
|---|---|---|---|
| A | COMPLIANT | NOT_RECOMMENDED | COMPLIANT_ALTERNATE (1,000 higher than C, about 0.08 percent) |
| B | NON_COMPLIANT_MANDATORY | NOT_RECOMMENDED | FAILED_MANDATORY |
| C | COMPLIANT | RECOMMENDED | PRIMARY_PICK (flag: CLOSE_CALL) |

Key points for the demo:
- B has the lowest quoted price (1,059,000) but is not recommended, because it fails a mandatory specification (concrete M20 instead of M25), has no steel grade, and excludes scaffolding.
- C is cheaper than A by only 1,000, so the system flags a close call.
- The user always makes the final decision.