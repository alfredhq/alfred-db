from sqlalchemy.orm import sessionmaker


Session = sessionmaker(autocommit=False, autoflush=False)
