import jinja2

meet_template = jinja2.Template('''
Meet Results\n==============\n
{% for event in events %}
Event {{ event.number }}: {{ event.name }}\n------------------------\n{% for result in event.results %}
{{ result.place or '-' }}. {{ result.athlete.name }} ({{ result.athlete.team }}) - {{ result.result or 'NT' }} {% if result.dq_code %}(DQ: {{ result.dq_code }}){% endif %}
{% endfor %}

{% endfor %}
''')

csv_template = jinja2.Template('''event_number,event_name,heat,athlete,team,result,place,dq_code,points,splits
{% for event in events %}{% for result in event.results %}{{event.number}},{{event.name}},{{result.heat}},{{result.athlete.name}},{{result.athlete.team}},{{result.result|default('NT')}},{{result.place|default('-')}},{{result.dq_code|default('')}},{{result.points|default('0')}},{{result.splits|join(';')}}
{% endfor %}{% endfor %}
''')
