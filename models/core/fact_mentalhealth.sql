{{ config(
    materialized='table'
) }}

select 
-- identifier
unique_id,

-- mental health factors
mental_health_consequence,
phys_health_consequence,
coworkers,
supervisor,
mental_health_interview,
phys_health_interview,
mental_vs_physical,
obs_consequence
from {{ source('mentalhealth_staging','stag_mentalhealth_data')}}