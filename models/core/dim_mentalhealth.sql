{{ config(
    materialized='table'
) }}

select 
-- identifier
unique_id,

-- mental health factors
family_history,
treatment,
work_interfere,
no_employees,
benefits,
care_options, 
wellness_program,
seek_help,
anonymity,
leave
from {{ source('mentalhealth_staging','stag_mentalhealth_data')}}