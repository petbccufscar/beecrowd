use std::io;

fn main() {
	let pi = 3.14159;

	let stdin = io::stdin();

	let mut buffer = String::new();

	stdin.read_line(&mut buffer).unwrap();

	let r: f64 = buffer.trim().parse().unwrap();

	println!("A={:.4}", r * r * pi);
}