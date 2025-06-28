---
name: "report_${from}_${to}.md"
params:
  from:
    required: true
  to:
    required: true
  file:
    default: ledger.j
---

# Finance Report from {from} to {to}

## Previous status:

{{hledger -f $file bal -e $from -t}}

## Expenses:

{{hledger -f $file reg expenses -b $from -e $to}}

## Ending balance:

{{hledger -f $file bal -e $to -t}}

## Transactions:

{{hledger -f $file print -b $from -e $to}}
