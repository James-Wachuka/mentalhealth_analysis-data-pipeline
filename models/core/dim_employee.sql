{{ config(
    materialized='table'
) }}

select 
-- identifier
unique_id,

-- employee details
Age,
gendertype,
Country,
state,
remote_work,
tech_company
from {{ source('mentalhealth_staging','stag_mentalhealth_data')}}





