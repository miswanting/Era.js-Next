New-Item -Path ..\erajs-backend\erajs\www -Target ..\erajs-frontend\dist -ItemType SymbolicLink
New-Item -Path ..\erajs-sdk\erajs -Target ..\erajs-backend\erajs -ItemType SymbolicLink