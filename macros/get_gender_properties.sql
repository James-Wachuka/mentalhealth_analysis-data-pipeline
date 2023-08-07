 {#
    This macro returns gender into three categories 
#}

{% macro get_gender_properties(Gender) -%}

    case {{ Gender }}
        when 'male' then 'male'
        when 'female' then 'female'
        when 'f' then 'female'
        when 'm' then 'male'
        else 'others'
    end

{%- endmacro %}

              