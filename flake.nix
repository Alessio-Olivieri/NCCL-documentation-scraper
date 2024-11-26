{
  description = "A flake for scraping NVIDIA NCCL documentation";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = [
            pkgs.python3
            pkgs.python3Packages.requests
            pkgs.python3Packages.beautifulsoup4
          ];
        };

        packages.${system}.default = pkgs.stdenv.mkDerivation {
          pname = "nccl-doc-scraper";
          version = "0.1.0";

          src = ./.;

          buildInputs = [
            pkgs.python3
            pkgs.python3Packages.requests
            pkgs.python3Packages.beautifulsoup4
          ];

          buildPhase = ''
            mkdir -p $out/bin
            cp scrape_nccl_docs.py $out/bin/
          '';

          installPhase = ''
            wrapProgram \$out/bin/scrape_nccl_docs.py --prefix PYTHONPATH : \${pkgs.python3Packages.requests}/lib/python3.9/site-packages:\${pkgs.python3Packages.beautifulsoup4}/lib/python3.9/site-packages
          '';

          meta = with pkgs.lib; {
            description = "A script to scrape NVIDIA NCCL documentation";
            license = licenses.mit;
            maintainers = with maintainers; [ yourGitHubUsername ];
          };
        };
      });
}

