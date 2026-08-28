'use client';

import { Radar, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis, ResponsiveContainer, Tooltip } from 'recharts';
import { SkillScore } from '@/lib/api';

interface SkillRadarChartProps {
  skills: SkillScore[];
}

export default function SkillRadarChart({ skills }: SkillRadarChartProps) {
  const data = skills.map(skill => ({
    name: skill.skill_name.length > 20
      ? skill.skill_name.substring(0, 18) + '…'
      : skill.skill_name,
    score: Math.round(skill.score * 100),
    fullMark: 100,
  }));

  return (
    <div style={{ width: '100%', height: 300 }}>
      <ResponsiveContainer>
        <RadarChart data={data} cx="50%" cy="50%" outerRadius="70%">
          <PolarGrid
            stroke="rgba(255,255,255,0.06)"
            strokeDasharray="3 3"
          />
          <PolarAngleAxis
            dataKey="name"
            tick={{
              fill: '#94a3b8',
              fontSize: 11,
              fontFamily: 'Inter',
            }}
          />
          <PolarRadiusAxis
            angle={30}
            domain={[0, 100]}
            tick={{ fill: '#64748b', fontSize: 10 }}
            axisLine={false}
          />
          <Radar
            name="Skor"
            dataKey="score"
            stroke="#6366f1"
            fill="#6366f1"
            fillOpacity={0.15}
            strokeWidth={2}
            dot={{
              r: 4,
              fill: '#6366f1',
              stroke: '#818cf8',
              strokeWidth: 2,
            }}
          />
          <Tooltip
            contentStyle={{
              background: 'rgba(17, 24, 39, 0.95)',
              border: '1px solid rgba(99, 102, 241, 0.3)',
              borderRadius: '8px',
              color: '#f1f5f9',
              fontSize: '0.85rem',
              fontFamily: 'Inter',
            }}
            formatter={(value) => [`${value}%`, 'Skor']}
          />
        </RadarChart>
      </ResponsiveContainer>
    </div>
  );
}
