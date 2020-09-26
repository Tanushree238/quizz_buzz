from app import app
from flask import render_template, request,url_for,jsonify

@app.route('/')
def home():
	questions=[]
	f = list(open("app/q.txt", "r"))
	h = list(open("app/hash_Tags.txt", "r"))
	for x in range(20):
		question={}
		question["no."]=x+1
		question["hashtag"]=h[x].strip("\n")
		question["statement"]=f[x*4+0].strip("\n")[2:]
		question["options"]=f[x*4+1].strip("\n")
		question["answer"]=f[x*4+2].strip("\n")[2:]
		questions.append(question)
	print(questions)
	return render_template('home.html',questions=questions)


@app.route('/get_result/<string:ans_id>',methods=['GET'])
def get_result(ans_id):
	h = list(open("app/hash_Tags.txt", "r"))
	id=int(ans_id.split("_")[1])
	hashtag=h[id+20]
	with open("app/"+ans_id+".txt",'r',encoding="utf8") as f:
		result=f.read()
	type,content=result.split("|")
	print(type,content)
	return jsonify({'id':ans_id,'type':type,'content':content,'hashtag':hashtag})
	

