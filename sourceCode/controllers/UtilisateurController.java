package controllers;

import java.util.List;
import models.Utilisateur;
import repository.UtilisateurRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;


@RestController
@RequestMapping("/api/utilisateur")
@CrossOrigin(origins = "*")
public class UtilisateurController {

    
	@Autowired
	private UtilisateurRepository utilisateurRepository;

    
	@GetMapping 
	public List<Utilisateur> getAllUtilisateurs() {
	    return utilisateurRepository.findAll();
	}
	
	@GetMapping("/{id}")
	public ResponseEntity<Utilisateur> getUtilisateurById(@PathVariable Integer id) {
	    Utilisateur utilisateur = utilisateurRepository.findById(id).orElseThrow(() -> new Exception("Utilisateur avec l' id " + id + " n'existe pas"));
	    return ResponseEntity.ok(utilisateur);
	}
	
	@PostMapping 
	public Utilisateur saveUtilisateur(@RequestBody Utilisateur newUtilisateur) {
	    return utilisateurRepository.save(newUtilisateur);
	}
	
	@PutMapping("/{id}") 
	public Utilisateur updateUtilisateur(@PathVariable Integer id, @RequestBody Utilisateur updatedUtilisateur) {
	    Utilisateur utilisateur = utilisateurRepository.findById(id).orElseThrow(() -> new Exception("Utilisateur avec l' id " + id + " n'existe pas"));
	    updateUtilisateur.setIdUtilisateur(id);
	    return udpateUtilisateur.save(updatedUtilisateur);
	}
	
	@DeleteMapping("/{id}") 
	public ResponseEntity<Map<String, Boolean>> deleteUtilisateur(@PathVariable Integer id) {
	    Utilisateur utilisateur = utilisateurRepository.findById(id).orElseThrow(() -> new Exception("Utilisateur avec l' id " + id + " n'existe pas"));
	    utilisateurRepository.delete(utilisateur);
	    Map<String, Boolean> response = new HashMap<>();
	    response.put("deleted", Boolean.TRUE);
	    return ResponseEntity.ok(response);
	}
	
}