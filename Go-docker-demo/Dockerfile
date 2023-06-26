# Dockerfile
# Build stage
FROM golang:1.16 AS build

WORKDIR /app

COPY main.go /app

RUN go build -o myapp

# Final stage
FROM scratch

COPY --from=build /app/myapp /

CMD ["/myapp"]
