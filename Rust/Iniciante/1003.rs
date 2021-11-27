use std::io;

fn main() {
	let stdin = io::stdin();

	let mut a_buffer = String::new();
	let mut b_buffer = String::new();

	stdin.read_line(&mut a_buffer).unwrap();
	stdin.read_line(&mut b_buffer).unwrap();

	let a: i32 = a_buffer.trim().parse().unwrap();
	let b: i32 = b_buffer.trim().parse().unwrap();

	println!("SOMA = {}", a + b);
}