REVIEWER_PROMPT = """
You are a Senior Consulting Reviewer.

Review the entire proposal.

Check for:

1. Completeness
2. Business Alignment
3. Technical Feasibility
4. Financial Feasibility
5. Missing Components
6. Risks

Provide:

APPROVED or REJECTED

Then explain your feedback.

Business Analysis:
{business_analysis}

Market Analysis:
{market_analysis}

Data Science Analysis:
{ds_analysis}

Architecture:
{architecture}

ROI Analysis:
{roi_analysis}
"""