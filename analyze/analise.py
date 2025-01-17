import uuid
from helper import get_pdf_paths, read_pdf, extract_data_analysis
from database import AnalyzeDatabase
from ai import GroqClient
from models.resum import Resum
from models.file import File

database = AnalyzeDatabase()
ai = GroqClient()
job = database.get_job_by_name("Vaga de Programador")

cv_paths = get_pdf_paths(dir="curriculos")

for path in cv_paths:
    content = read_pdf(path)

    resum = ai.resume_cv(content)
    print(resum)

    opnion = ai.generate_opnion(content, job)
    print(opnion)

    score = ai.generate_score(resum, job)
    print(score)

    resum_schema = Resum(
        id=str(uuid.uuid4()),
        job_id=job.get("id"),
        content=resum,
        file=str(path),
        opnion=opnion,
    )

    file = File(file_id=str(uuid.uuid4()), job_id=job.get("id"))

    analysis = extract_data_analysis(resum, resum_schema.job_id, resum_schema.id, score)

    database.resums.insert(resum_schema.model_dump())
    database.analysis.insert(analysis.model_dump())
    database.files.insert(file.model_dump())
