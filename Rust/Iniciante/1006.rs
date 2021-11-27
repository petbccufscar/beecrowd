use std::io;

fn main() {
	let stdin = io::stdin();

	let mut a_buffer = String::new();
	let mut b_buffer = String::new();
	let mut c_buffer = String::new();

	stdin.read_line(&mut a_buffer).unwrap();
	stdin.read_line(&mut b_buffer).unwrap();
	stdin.read_line(&mut c_buffer).unwrap();

	let a: f64 = a_buffer.trim().parse().unwrap();
	let b: f64 = b_buffer.trim().parse().unwrap();
	let c: f64 = c_buffer.trim().parse().unwrap();

	println!("MEDIA = {:.1}", (a * 2.0 + b * 3.0 + c * 5.0) / 10.0);
}