## How This Project Is Used (Cloud & SQL Perspective)

### The Problem

In many data platforms, pipelines run on a schedule (hourly, daily, or near real-time).  
A common design mistake is using **full data reloads**, where the pipeline reads *all records* every time it runs.

This leads to:
- Increased execution time
- Large data scans
- Higher cloud costs (BigQuery, Dataflow, Snowflake, Glue)

---

### The Idea Behind This Project

This project demonstrates **why Change Data Capture (CDC)** is a better approach than **FULL loads**, using **measurable metrics** instead of assumptions.

Rather than only moving data, the pipeline **measures**:
- Execution time  
- Data volume processed  
- Estimated cost  

This allows data engineers to **quantify the impact** of architectural decisions.

---

## How It Works

### FULL Load

```sql
SELECT * FROM source_table;
