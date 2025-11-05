async def getAssessments(client_id: UUID, db: Session = Depends(get_async_session)):
    evaluation_id_data = await getEvaluationId(client_id, db)
    evaluation_id = evaluation_id_data['data']
    evaluation_dimensions_data = await getEvluationDimensions(evaluation_id, db)
    evaluation_dimensions = evaluation_dimensions_data['data']

    assessment = []
    for dimension in evaluation_dimensions:
        print(f"\n\n dimension {dimension} \n\n")
        print(f"\n\n dimension dict {dimension.__dict__} \n\n")

