class DimensionsEvaluation(Base):
    __tablename__ = "dimensions_evaluation"
    id = Column(Integer, primary_key=True)
    dimension_id = Column(Integer, ForeignKey('dimension.id'))
    evaluation_id = Column(Integer, ForeignKey('evaluation.id'))
    questions = Column(String, nullable=False)
    selected = Column(Boolean, default=False)

