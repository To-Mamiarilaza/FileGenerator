package repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import models.Language;

@Repository
public interface LanguageRepository extends JpaRepository<Language, Integer>{

}
