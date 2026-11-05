{{ config(materialized='table') }}

SELECT
    employee_id,
    -- Indicateur : L'employé est-il parti ? (1 = Oui, 0 = Non)
    CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END AS has_left,
    monthly_income,
    -- Indicateur : Fait-il des heures sup ? (1 = Oui, 0 = Non)
    CASE WHEN over_time = 'Yes' THEN 1 ELSE 0 END AS is_over_time,
    job_satisfaction,
    work_life_balance
FROM {{ ref('stg_employees') }}