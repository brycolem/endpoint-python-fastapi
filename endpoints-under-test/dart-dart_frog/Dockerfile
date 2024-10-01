FROM dart:stable AS build

WORKDIR /app

COPY pubspec.* ./
RUN dart pub get
RUN dart pub global activate dart_frog_cli

COPY . .

RUN dart pub get --offline
RUN dart_frog build
RUN dart compile exe build/bin/server.dart -o bin/server

FROM alpine:latest
COPY --from=build /runtime/ /
COPY --from=build /app/bin/server /app/bin/

EXPOSE 8001

CMD ["/app/bin/server"]