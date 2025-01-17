import uuid
from models.job import Job
from database import AnalyzeDatabase

database = AnalyzeDatabase()

name = "Vaga de Auxiliar de Vida"

activities = """
Acompanhar e auxiliar pessoas com necessidades especiais ou limitações em suas atividades diárias
Oferecer suporte em tarefas como locomoção, alimentação, higiene pessoal e lazer
Auxiliar na organização e administração de medicamentos, conforme orientação médica
Promover a integração social e o bem-estar físico e emocional do assistido
Manter a comunicação com familiares ou responsáveis sobre a rotina do assistido
Participar de reuniões e treinamentos para aprimorar a qualidade do atendimento
"""

prequisites = """
Ensino médio completo
Experiência em assistência a pessoas com necessidades especiais ou idosos
Empatia, paciência e habilidade para lidar com diferentes perfis
Capacidade física para tarefas de suporte e mobilização
Boa comunicação e atitude responsável
"""

differentials = """
Curso ou certificação em Cuidador ou áreas relacionadas
Experiência com crianças ou adultos com autismo, paralisia cerebral ou deficiência auditiva
Habilidade para lidar com situações emergenciais
Conhecimento em primeiros socorros
Disponibilidade para trabalho em horários flexíveis
"""

job = Job(
    id=str(uuid.uuid4()),
    name=name,
    main_activities=activities,
    prerequisites=prequisites,
    differentials=differentials,
)

database.jobs.insert(job.model_dump())
