rewrite
   ↓
router
   ├── direct
   │      ↓
   │   executor
   │      ↓
   │   reflector
   │      ↓
   │    answer
   │
   └── planner
          ↓
       executor
          ↓
       reflector
          ↓
      replan? ──► replanner ──► executor
          │
          ▼
        answer