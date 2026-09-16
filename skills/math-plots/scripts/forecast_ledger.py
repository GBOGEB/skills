#!/usr/bin/env python3
import argparse, json
from pathlib import Path
def main():
    p=argparse.ArgumentParser(); p.add_argument('ledger',type=Path); p.add_argument('--actual',type=float); p.add_argument('--pulse'); ns=p.parse_args(); d=json.loads(ns.ledger.read_text())
    if ns.actual is None: print(json.dumps(d,indent=2)); return
    pending=[x for x in d.get('predictions',[]) if x.get('target_pulse')==ns.pulse and x.get('actual') is None]
    if not pending: raise SystemExit('no pending prediction for pulse')
    for x in pending:
        x['actual']=ns.actual; x['signed_error']=ns.actual-x['prediction']; x['absolute_error']=abs(x['signed_error'])
    errs=[x['absolute_error'] for x in d['predictions'] if x.get('absolute_error') is not None]
    d['metrics']={'mae':sum(errs)/len(errs),'n_scored':len(errs)}
    ns.ledger.write_text(json.dumps(d,indent=2)+'\n'); print(json.dumps(d['metrics'],indent=2))
if __name__=='__main__': main()
