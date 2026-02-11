SELECT *
FROM raw_data
WHERE income > 0
  AND credit_utilization BETWEEN 0 AND 1
  AND missed_payments >= 0
  AND account_age >= 0;
