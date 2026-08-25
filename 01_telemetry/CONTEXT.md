# Stage 01: Telemetry & Mesh Health
## Input
- Supabase live telemetry stream
- Local dev `/health` and VPS node endpoints

## Process
- Probe mesh nodes every interval.
- Aggregate latency, CPU/RAM load, and tool execution success rates.

## Output
- Structured JSON snapshot at `output/latest_mesh_health.json`.
