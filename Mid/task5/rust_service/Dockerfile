FROM rust:1.80-slim AS builder

RUN apt-get update && apt-get install -y pkg-config libssl-dev && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY . .

RUN cargo build --release

FROM debian:bookworm-slim
WORKDIR /app

COPY --from=builder /usr/src/app/target/release/task5 /app/task5

RUN useradd -m rustuser
USER rustuser

CMD ["./task5"]