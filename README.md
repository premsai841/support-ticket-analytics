# Support Ticket Analytics

> A support-operations analytics project for measuring ticket volume, SLA performance, resolution time, backlog, and agent workload.

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-analysis-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org/)

## Purpose

Support teams need reliable operational metrics before they can improve customer experience. This project turns ticket-level data into a compact weekly performance report.

## Metrics

- Total tickets
- Open vs. resolved backlog
- SLA compliance rate
- Average resolution time
- Priority distribution
- Category distribution
- Agent workload

## Structure

```text
support-ticket-analytics/
├── data/tickets.csv
├── src/analyze_tickets.py
├── requirements.txt
└── README.md
```

## Run

```bash
pip install -r requirements.txt
python src/analyze_tickets.py
```

## Scope

Uses synthetic data for demonstration. No real customer or company information is included.

## Author

**Prem Sai Bachchala** — Customer Support / Customer Success analytics portfolio project.
