'use client';

import { RoleInfo } from '@/lib/api';
import styles from './RoleSelector.module.css';

interface RoleSelectorProps {
  roles: RoleInfo[];
  selectedRole: string;
  onRoleSelect: (roleId: string) => void;
  selectedLevel: string;
  onLevelSelect: (level: string) => void;
}

const ROLE_ICONS: Record<string, string> = {
  'game-dev': '🎮',
  'backend': '⚙️',
  'frontend': '🎨',
  'devops': '🚀',
  'devops-engineer': '🚀',
  'android': '📱',
  'ios': '🍎',
  'data-analyst': '📊',
  'data-engineer': '🔧',
  'machine-learning': '🤖',
  'mlops': '🧪',
  'ai-engineer': '🧠',
  'cyber-security': '🔒',
  'network-engineer': '🌐',
  'qa-engineer': '✅',
  'api-design': '🔌',
};

const LEVEL_LABELS: Record<string, { label: string; color: string }> = {
  junior: { label: 'Junior', color: 'var(--accent-emerald)' },
  mid: { label: 'Mid', color: 'var(--accent-amber)' },
  senior: { label: 'Senior', color: 'var(--accent-rose)' },
};

export default function RoleSelector({
  roles,
  selectedRole,
  onRoleSelect,
  selectedLevel,
  onLevelSelect,
}: RoleSelectorProps) {
  return (
    <div className={styles.container}>
      <label className={styles.label}>Hedef Rol</label>
      <div className={styles.roleGrid}>
        {roles.map((role) => (
          <button
            key={role.role_id}
            className={`${styles.roleCard} ${selectedRole === role.role_id ? styles.roleCardActive : ''}`}
            onClick={() => onRoleSelect(role.role_id)}
            type="button"
            id={`role-${role.role_id}`}
          >
            <span className={styles.roleIcon}>
              {ROLE_ICONS[role.role_id] || '💼'}
            </span>
            <span className={styles.roleName}>{role.title.replace(/^(Junior|Mid|Senior)\s+/i, '')}</span>
            <span className={styles.skillCount}>{role.skill_count} skill</span>
          </button>
        ))}
      </div>

      {selectedRole && (
        <div className={styles.levelContainer}>
          <label className={styles.label}>Seviye</label>
          <div className={styles.levelGroup}>
            {Object.entries(LEVEL_LABELS).map(([level, config]) => (
              <button
                key={level}
                className={`${styles.levelBtn} ${selectedLevel === level ? styles.levelBtnActive : ''}`}
                onClick={() => onLevelSelect(level)}
                type="button"
                id={`level-${level}`}
                style={{
                  '--level-color': config.color,
                } as React.CSSProperties}
              >
                {config.label}
              </button>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
