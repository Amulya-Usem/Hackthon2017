from . config import initiateDb


def fetchTrainingData(training_properties):
	db = initiateDb()
	bucket = []
	historical_data = list(db.users.find({}, {"ppmLevel": 1, "bacteriaTypeInAir":1, "phLevel":1, "bacteriaTypeInWater":1, "foodFiberContent":1, "_id": 0}))
	for doc in historical_data:
		doc  = doc.values()
		bucket.append(doc)
	return bucket

def fetchLabels(training_properties):
	db = initiateDb()
	historical_data = list(db.users.find({}, {"_id": 0, "diseaseType":1}))
	labels = []
	for doc in historical_data:
		labels.append(doc.get('diseaseType'))
	return labels		
