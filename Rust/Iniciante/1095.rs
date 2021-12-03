use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	
	for i in 0..13 {
		println!("I={} J={}", 1 + i * 3, 60 - i * 5);
	}

	Ok(())
}