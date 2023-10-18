use std::sync::Mutex;
use actix_web::{web, App, HttpResponse, HttpServer, Responder};

struct AppState {
    counter: Mutex<i32>, // <- Mutex is necessary to mutate safely across threads
}

async fn increment(data: web::Data<AppState>) -> impl Responder {
    let mut counter = data.counter.lock().unwrap(); // <- get counter's MutexGuard
    *counter += 1; // <- access counter inside MutexGuard
    HttpResponse::Ok().body(format!("Counter: {}", counter)) // <- response with count
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        let app_state = web::Data::new(AppState {
            counter: Mutex::new(0),
        });

        App::new()
            .app_data(app_state.clone()) // <- register the created data
            .route("/", web::post().to(increment))
    })
    .bind("127.0.0.1:8080")?
    .run()
    .await
}