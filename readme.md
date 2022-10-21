# upgrade pip :
>>python.exe -m pip install --upgrade pip

# virtual environment :
python -m venv venv
>>venv\Scripts\activate

# poetry :
>>poetry init

# poetry installing packages :
>>poetry add fastapi SQLAlchemy psutil schedule requests pydantic uvicorn

# run fastapi :
>>cd app
>>python -m uvicorn main:app --reload

# documentation :
- Swagger : route/docs
<br />
- redoc : route/redoc

# git :
>>git init
<br />
>>git checkout -b [num][name]
<br />
>>git status
<br />
goto: https://gitignore.io/ (python,windows,macos,vim,visualstudiocode,linux)
<br />
copy all to .gitignore file
<br />
>>git status
<br />
>>git add .
<br />
>>git commit -m "first commit with initial api setup"
<br />
>>git remote add origin [url]
<br />
>>git remote -v
<br />
>>git push -u origin [num]][name]
<br />
- to update and add new branches :
<br />
git checkout -b [num][name]
<br />
>>git status
<br />
>>git add .
<br />
>>git commit -m "sixth commit with initial api setup"
<br />
>>git push -u origin [num]][name]