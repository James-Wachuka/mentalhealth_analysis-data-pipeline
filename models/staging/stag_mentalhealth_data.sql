{{ config(
    materialized='table'
) }}

select 
-- identifier
rand() as unique_id,

-- use macro for coverting gender types
{{ get_gender_properties('Gender') }} as gendertype,

*
from {{ source('mentalhealth_staging','mental_health_table_1')}}
