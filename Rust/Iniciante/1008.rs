use std::io;

fn main() {
	let stdin = io::stdin();

	let mut number_buffer = String::new();
	let mut hours_buffer = String::new();
	let mut value_buffer = String::new();

	stdin.read_line(&mut number_buffer).unwrap();
	stdin.read_line(&mut hours_buffer).unwrap();
	stdin.read_line(&mut value_buffer).unwrap();

	let number: i32 = number_buffer.trim().parse().unwrap();
	let hours: f64 = hours_buffer.trim().parse().unwrap();
	let value: f64 = value_buffer.trim().parse().unwrap();

	println!("NUMBER = {}", number);
	println!("SALARY = U$ {:.2}", hours * value);
}