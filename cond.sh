CODE= $(curl -v --stderr deploy.log -w "%{http_code}\n" -F password=$1 -F file=@build/index.html -F user=$2 https://cs.uns.edu.ar/~jose.moyano/index.php)

if [ CODE -ne 200 ]
then exit 1
fi