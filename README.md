## How This Project Is Used (Cloud & SQL Perspective)

### The Problem

In many data platforms, pipelines run on a fixed schedule (hourly, daily, or near real-time).  
A common design approach is using **full data reloads**, where all records are read every time the pipeline runs.

This often leads to:
- Increased execution time
- Large data scans
- Higher cloud costs (e.g., BigQuery, Dataflow, Snowflake, Glue)

---

### The Idea Behind This Project

This project demonstrates **why Change Data Capture (CDC)** can be more efficient than **FULL loads**, using **measurable metrics** instead of assumptions.

Instead of only moving data, the pipeline measures:
- Execution time
- Data volume processed
- Estimated cost

This allows data engineers to **quantify the impact** of architectural decisions rather than relying on intuition.

---

### How It Works

#### FULL Load

```sql
SELECT * FROM source_table;
