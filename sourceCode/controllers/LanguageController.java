package controllers;

import java.util.List;
import models.Language;
import repository.LanguageRepository;
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
@RequestMapping("/api/language")
@CrossOrigin(origins = "*")
public class LanguageController {

    
	@Autowired
	private LanguageRepository languageRepository;

    
	@GetMapping 
	public List<Language> getAllLanguages() {
	    return languageRepository.findAll();
	}
	
	@GetMapping("/{id}")
	public ResponseEntity<Language> getLanguageById(@PathVariable Integer id) {
	    Language language = languageRepository.findById(id).orElseThrow(() -> new Exception("Language avec l' id " + id + " n'existe pas"));
	    return ResponseEntity.ok(language);
	}
	
	@PostMapping 
	public Language saveLanguage(@RequestBody Language newLanguage) {
	    return languageRepository.save(newLanguage);
	}
	
	@PutMapping("/{id}") 
	public Language updateLanguage(@PathVariable Integer id, @RequestBody Language updatedLanguage) {
	    Language language = languageRepository.findById(id).orElseThrow(() -> new Exception("Language avec l' id " + id + " n'existe pas"));
	    updateLanguage.setIdLanguage(id);
	    return udpateLanguage.save(updatedLanguage);
	}
	
	@DeleteMapping("/{id}") 
	public ResponseEntity<Map<String, Boolean>> deleteLanguage(@PathVariable Integer id) {
	    Language language = languageRepository.findById(id).orElseThrow(() -> new Exception("Language avec l' id " + id + " n'existe pas"));
	    languageRepository.delete(language);
	    Map<String, Boolean> response = new HashMap<>();
	    response.put("deleted", Boolean.TRUE);
	    return ResponseEntity.ok(response);
	}
	
}