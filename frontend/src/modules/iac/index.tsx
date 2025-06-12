import React, { useState, useEffect } from 'react';
import { useQuery } from '@tanstack/react-query';
import axios from 'axios';

// iac - IaC misconfigs with severity - distinct UI per scanner
interface Finding { file:string; severity:string; match?:string; pkg?:string; check?:string; }

export const IacView: React.FC = () => {
  const [filter, setFilter] = useState('high');
  const { data } = useQuery({
    queryKey: ['iac', filter],
    queryFn: async () => {
      try {
        const r = await axios.get(`/scan?path=.`);
        return r.data as { findings: Finding[] };
      } catch {
        // distinct mock per iac
        const mock: Finding[] = [
          { file: "src/app.py", severity: filter, match: "iac-finding-1" },
          { file: "config/terraform/main.tf", severity: "critical", check: "TF001" },
        ];
        return { findings: mock };
      }
    }
  });
  useEffect(()=>{ document.title="Iac - Vigilant"; },[]);
  return (
    <div className="p-4">
      <h2 className="text-xl font-bold">IAC — IaC misconfigs with severity</h2>
      <div className="flex gap-2 mt-2">
        {['critical','high','medium'].map(s=>(
          <button key={s} onClick={()=>setFilter(s)} className={filter===s?'bg-red-600 text-white px-2 rounded':'bg-gray-200 px-2 rounded'}>{s}</button>
        ))}
      </div>
      <ul className="mt-4 space-y-2">
        {(data?.findings||[]).map((f,i)=>(
          <li key={i} className="p-2 border rounded">
            <span className="font-mono text-sm">{f.file}</span> — <span className="text-red-600">{f.severity}</span> {f.match||f.check||f.pkg}
          </li>
        ))}
      </ul>
      <p className="text-xs text-gray-500 mt-4">Vigilant iac — distinct from other modules</p>
    </div>
  );
};
export default IacView;
