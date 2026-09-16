#!/usr/bin/env python3
import argparse, json, sys
from pathlib import Path
ALLOWED={"CORE","ADVANCED","DEEP_DIVE","STRETCH"}
def main():
    p=argparse.ArgumentParser(); p.add_argument('envelope',type=Path); ns=p.parse_args(); d=json.loads(ns.envelope.read_text())
    req=['schema','skill','task_id','source_repo','source_ref','topic','maturity','plot_purpose','authority_transfer']; miss=[k for k in req if k not in d]
    if miss: raise SystemExit('missing fields: '+','.join(miss))
    if d['schema']!='gbogeb.skill.invoke.v1' or d['skill']!='math-plots': raise SystemExit('wrong schema or skill')
    if d['maturity'] not in ALLOWED: raise SystemExit('invalid maturity')
    if d['authority_transfer'] is not False: raise SystemExit('authority_transfer must remain false')
    json.dump({'schema':'gbogeb.skill.receipt.v1','skill':'math-plots','task_id':d['task_id'],'source_repo':d['source_repo'],'source_ref':d['source_ref'],'resolved_skill_path':'skills/math-plots/SKILL.md','authority_transfer':False,'status':'PASS_SKILL_RESOLUTION'},sys.stdout,indent=2); print()
if __name__=='__main__': main()
