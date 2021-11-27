use std::io;

fn main() {
	let stdin = io::stdin();

	let mut a_buffer = String::new();
	let mut b_buffer = String::new();

	stdin.read_line(&mut a_buffer).unwrap();
	stdin.read_line(&mut b_buffer).unwrap();

	let a: f64 = a_buffer.trim().parse().unwrap();
	let b: f64 = b_buffer.trim().parse().unwrap();

	println!("MEDIA = {:.5}", (a * 3.5 + b * 7.5) / 11.0);
}