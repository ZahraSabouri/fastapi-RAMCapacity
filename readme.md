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
- redoc : route/redoc

# git :
>>git init
>>git checkout -b [num][name]
>>git status
goto: https://gitignore.io/ (python,windows,macos,vim,visualstudiocode,linux)
copy all to .gitignore file
>>git status
>>git add .
>>git commit -m "first commit with initial api setup"
>>git remote add origin [url]
>>git remote -v
>>git push -u origin [num]][name]
