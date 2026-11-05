{{ config(materialized='table') }}

SELECT
    employee_id,
    age,
    gender,
    department,
    job_role,
    job_level,
    education_field,
    marital_status,
    distance_from_home,
    years_at_company,
    years_in_current_role
FROM {{ ref('stg_employees') }}