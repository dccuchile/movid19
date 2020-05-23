train_data = [
    # Cluster 1-2: Efectos adversos vacuna influenza
    # idx: 0
    [
        'vacuna contra la influenza',
        'Porque me había puesto la vacuna contra la influenza y estaba evaluando',
        'mis sintomas pueden deberse a la vacuna de la influenza',
        'Porque me puse la vacuna de la influenza',
        'Fue dolor de cabeza luego de colocarme vacuna influenza',
        'Efectos adversos vacuna influenza',
    ],

    # Cluster 1-2: Sintomas habituales o atribuye a otra causa
    # idx: 1
    [
        'siempre sufro dolores de cabeza',
        'dolores que he tenido siempre',
        'normalmente sufro de dolores de cabeza',
        'porque sufro de jaquecas desde siempre',
        'sufro de migrañas por mi epilepsia',
        'Sufro de cefalea ocasional por la hipertensión',
        'Sintomas habituales o atribuye a otra causa',
    ],
    # idx: 2
    [
        'soy asmática y tengo estos síntomas por la alergia',
        'sol alérgica y estos síntomas son usuales',
        'siempre tengo tos',
        'soy fumadora y siempre tengo tos',
        'Siempre estoy con tos, tengo asma bronquial',
        'Siempre toso un poquito, es habitual ,no es resfrío',
        'Fumo, cuesta mucho que se vaya la tos',
        'Por que lo atribuyo a consumo de cigarrillo, estrés y ejecución de rutinas de ejercicios',
        'Lo atribuyo a otra causa',
        'Sintomas habituales o atribuye a otra causa',
    ],
    # idx: 3
    [
        'Suelo tener cefalea y dolores musculares',
        'Siempre e tenido dolores musculares en las articulaciones',
        'no es anormal en mí tener dolores musculares',
        'Son dolores habituales a esta edad',
        'Sufro fibromialgia y los Dolores son habituales',
        'Estoy en tratamiento por fibromialgia y me doy cuenta que si me estreso demasiado, me duele la cabeza.',
        'Sintomas habituales o atribuye a otra causa',
    ],
    # idx: 4
    [
        'Sufro de reflujo gastrico y me parecen normal los sintomas en mi vida',
        'Sufro de reflujo laringofaringeo',
        'Diagnostico de reflujo',
        'Sintomas habituales o atribuye a otra causa',
    ],
    # idx: 5
    [
        'Es algo relativamente habitual en ',
        'Es muy frecuente en mi , desde siempre',
        'es por momentos y habitual en mi',
        'Porque es habitual',
        'Sintomas habituales o atribuye a otra causa',
        'Es parte de una condicion medica pre existente',
    ],
    # idx: 6
    [
        'lo atribuyo al estres',
        'lo atribuyo al cansancio',
        'asocio el síntoma al estres',
        'Sintomas habituales o atribuye a otra causa',
    ],
    
    # Cluster 3: Sintomas leves o transitorios
    # idx: 7
    [
        'los síntomas pasaron solo fue un día',
        'los síntomas pasaron al otro día',
        'los síntomas han desaparecido',
        'fueron síntomas leves que duraron pocos días',
        'Fue un día aislado, no han habiado más síntomas',
        'Porque ha sido leve y esporádico',
        'fue muy leve',
        'muy reciente y leve',
        'fue transitorio',
        'duraron solo un día',
        'fue solo un día',
        'Porque era un malestar pasajero',
        'Es solo un tema pasajero',
        'Síntomas leves o transitorios',
        'Síntoma duró horas y no reapareció',
        'Fue de corta duración, solo un par de horas',
        'Porque se alivió con paracetamol y no volvió a presentarse',
    ], 
    # idx: 8
    [
        'no tengo fiebre',
        'no presentaba fiebre',
        'sin fiebre no me atienden',
        'No he tenido fiebre',
        'Porque no he tenido sintomas',
        'no he tenido nada',
        'Sintomas leves o transitorios',
    ],

    # Cluster 4: Miedo a contagiarse
    # idx: 9
    [
        'porque me estaría exponiendo al salir de la casa',
        'miedo a salir de la casa',
        'prefiero no salir',
        'por temor a contagiarme en el consultorio',
        'posible contagio en un centro asistencial',
        'centros públicos pueden ser foco de infección mayor',
        'no quiero exponerme a ir a un centro de salud',
        'Porque creo que es más arriesgado asistir algún centro de salud y contagiarse',
        'Riesgo de contagio en centros de salud',
        'Posibilidad de contagio',
        'Temor al contagio',
        'Porque no me quiero exponer en un centro de salud, es peligroso',
        'Miedo a contagiarme en algún centro de salud',
        'Por miedo a contagiarme en el servicio de salud',
        'No quiero ir a un centro de salud y exponerme a quizás estar en un ambiente más propenso a que este el virus',
        'Miedo a contagiarse',
    ],

    # Cluster 5: Considera que no tiene riesgo
    # idx: 10
    [
        'Por que llevo casi un mes encerrada y no he te ido contacto con nadie',
        'No he tenido contacto llevo 1 mes en casa',
        'Porque estoy en cuarentena hace 1 mes. No he tenido contacto con el exterior. ',
        'no he tenido contacto con el exterior',
        'No he salido de la casa',
        'Porque no he tenido contacto estrecho con nadie',
        'No he estado en contacto con gente',
        'Porque he mantenido cuarentena preventiva y limitado el contacto a personas ajenas a mi grupo familiar al mínimo',
        'Porque hago cuarentena y no me pareció importante',
        'Considero que no tengo riesgo',
    ],

    # Cluster 6: Saturación del sistema de salud
    # idx: 11
    [
        'Dicen que los sistemas están colapsados',
        'Centros de salud congestionados',
        'Los centros asistenciales estan colapsados',
        'Sistema de salud colapsado',
        'Saturación del sistema sanitario',
        'Para no saturar el sistema de salud',
        'Para no saturar el sistema público',
        'Porque no quiero colapsar el sistema',
        'No colapsar el sistema de salud',
        'Saturación del sistema de salud',
    ],

    # Cluster 7: Examen previo negativo
    # idx: 12
    [
        'Porque ya me hice el test coronavirus hace 3 semanas y salió negativo',
        'Y porque me evalué el 06/04 y me hicieron el examen que salió negativo',
        'Me realice el PCR y estoy esperando el resultado',
        'Mi pcr de hace 1 semana es negativo',
        'Porque ya me hice el test coronavirus hace 3 semanas y salió negativo',
        'Pq consulté hace dos semanas, me hicieron el examen Covid-19 y salió negativo. ',
        'Examen previo negativo',
    ]
]

labels = [
    # Cluster 1: Sintomas habituales o atribuye a otra causa
    'Sintomas habituales o atribuye a otra causa',
    'Sintomas habituales o atribuye a otra causa',
    'Sintomas habituales o atribuye a otra causa',
    'Sintomas habituales o atribuye a otra causa',
    'Sintomas habituales o atribuye a otra causa',
    'Sintomas habituales o atribuye a otra causa',
    'Sintomas habituales o atribuye a otra causa',
    # Cluster 2: Sintomas leves o transitorios
    'Sintomas leves o transitorios',
    'Sintomas leves o transitorios',
    # Cluster 3: Miedo a contagiarse
    'Miedo a contagiarse',
    # Cluster 4: Considera que no tiene riesgo
    'Considera que no tiene riesgo',
    # Cluster 5: Saturación del sistema de salud
    'Saturación del sistema de salud',
    # Cluster 6: Examen previo negativo
    'Examen previo negativo',
]

labels_to_classes = ([1]*7) + [2]*2 + [3,4,5,6]

classes = [
    '',
    'Sintomas habituales o atribuye a otra causa',
    'Sintomas leves o transitorios',
    'Miedo a contagiarse',
    'Considera que no tiene riesgo',
    'Saturación del sistema de salud',
    'Examen previo negativo/positivo',
]
