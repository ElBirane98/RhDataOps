{{ config(materialized='view') }}

SELECT
    "EmployeeNumber"      AS employee_id,
    "Attrition"           AS attrition,
    "Age"                 AS age,
    "Gender"              AS gender,
    "Department"          AS department,
    "JobRole"             AS job_role,
    "JobLevel"            AS job_level,
    "MonthlyIncome"       AS monthly_income,
    "YearsAtCompany"      AS years_at_company,
    "YearsInCurrentRole"  AS years_in_current_role,
    "OverTime"            AS over_time,
    "JobSatisfaction"     AS job_satisfaction,
    "WorkLifeBalance"     AS work_life_balance,
    "EducationField"      AS education_field,
    "MaritalStatus"       AS marital_status,
    "DistanceFromHome"    AS distance_from_home
FROM {{ source('bronze', 'employees_raw') }}