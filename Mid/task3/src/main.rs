use std::io::{self, Write};

fn main() {
    println!("Rust Service for HoReCa is starting...");
    
    let table_id = 5;
    let price = calculate_reservation(table_id);
    
    println!("Reservation check for table {}: ${}", table_id, price);
    
    println!("Rust Service: Status OK");
}

fn calculate_reservation(id: i32) -> i32 {
    id * 10 + 50
}