# Etapa de construcción
FROM node:18-alpine AS build-stage

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de configuración de dependencias
COPY package.json package-lock.json ./

# Instalar las dependencias
RUN npm ci

# Copiar el resto de la aplicación
COPY . .

# Construir la aplicación para producción
RUN npm run build

# Etapa de producción
FROM nginx:stable-alpine AS production-stage

# Copiar los archivos construidos desde la etapa anterior
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Exponer el puerto en el que NGINX escuchará
EXPOSE 80

# Comando para ejecutar NGINX en primer plano
CMD ["nginx", "-g", "daemon off;"]