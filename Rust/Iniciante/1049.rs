use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();

	let mut c1 = String::new();
	let mut c2 = String::new();
	let mut c3 = String::new();

	stdin.read_line(&mut c1)?;
	stdin.read_line(&mut c2)?;
	stdin.read_line(&mut c3)?;

	let rc1 = c1.trim().as_ref();
	let rc2 = c2.trim().as_ref();
	let rc3 = c3.trim().as_ref();

	let classificacao = match rc1 {
		"vertebrado" => match rc2 {
			"ave" => match rc3 {
				"carnivoro" => "aguia",
				"onivoro"   => "pomba",
				_           => "",
			}
			"mamifero" => match rc3 {
				"onivoro"   => "homem",
				"herbivoro" => "vaca",
				_           => "",
			}
			_ => "",
		}
		"invertebrado" => match rc2 {
			"inseto" => match rc3 {
				"hematofago" => "pulga",
				"herbivoro"  => "lagarta",
				_            => "",
			}
			"anelideo" => match rc3 {
				"hematofago" => "sanguessuga",
				"onivoro"    => "minhoca",
				_            => "",
			}
			_ => "",
		}
		_ => "",
	};

	println!("{}", classificacao);

	Ok(())
}